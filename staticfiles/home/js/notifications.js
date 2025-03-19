document.addEventListener("DOMContentLoaded", function () {
    const notificationIcon = document.getElementById("notification-icon");
    const notificationList = document.getElementById("notification-list");
    const markAllReadButton = document.getElementById("mark-all-read");

    // Fetch notifications initially and set interval for regular fetching
    function fetchNotifications() {
        fetch("/notifications/fetch/")
            .then(response => response.json())
            .then(data => {
                notificationList.innerHTML = "";

                if (data.notifications.length > 0) {
                    data.notifications.forEach(notification => {
                        notificationList.innerHTML += `
                            <li>
                                <a href="${notification.link || '#'}">${notification.message}</a>
                                <small>${notification.created_at}</small>
                            </li>
                        `;
                    });
                    markAllReadButton.style.display = "block"; // Show "Mark all as read" if there are notifications
                } else {
                    notificationList.innerHTML = "<p>No new notifications</p>";
                    markAllReadButton.style.display = "none"; // Hide if no notifications
                }

                document.getElementById("notification-count").textContent = data.unread_count;
            });
    }

    // Show notifications and "Mark All as Read" button only when icon is clicked
    notificationIcon.addEventListener("click", function () {
        notificationList.style.display = notificationList.style.display === "block" ? "none" : "block";
        markAllReadButton.style.display = "block";
        fetchNotifications(); // Refresh notifications when dropdown is opened
    });

    // Mark all notifications as read
    markAllReadButton.addEventListener("click", function () {
        fetch("/notifications/mark_all_as_read/", {
            method: "POST",
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        }).then(() => fetchNotifications());
    });

    // Hide the dropdown if clicked outside
    document.addEventListener("click", function (event) {
        if (!notificationIcon.contains(event.target) && !notificationList.contains(event.target)) {
            notificationList.style.display = "none";
        }
    });

    // Utility function to get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
