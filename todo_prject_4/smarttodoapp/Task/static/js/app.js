const token =
localStorage.getItem("access");


// Dashboard Data

async function loadDashboard() {

    const response =
    await fetch(
        "/api/dashboard/",
        {
            headers:{
                Authorization:
                `Bearer ${token}`
            }
        }
    );

    const data =
    await response.json();

    document.getElementById(
        "totalTasks"
    ).innerText =
    data.total_tasks;

    document.getElementById(
        "completedTasks"
    ).innerText =
    data.completed_tasks;

    document.getElementById(
        "pendingTasks"
    ).innerText =
    data.pending_tasks;
}


// Load Tasks

async function loadTasks(){

    const response =
    await fetch(
        "/api/tasks/",
        {
            headers:{
                Authorization:
                `Bearer ${token}`
            }
        }
    );

    const tasks =
    await response.json();

    let html = "";

    tasks.forEach(task => {

        html += `

        <div class="card task-card shadow">

            <div class="card-body">

                <h5>${task.title}</h5>

                <p>${task.description}</p>

                <span class="badge bg-primary">

                    ${task.priority}

                </span>

            </div>

        </div>

        `;

    });

    document.getElementById(
        "taskList"
    ).innerHTML =
    html;
}


// Create Task

async function createTask(){

    const title =
    document.getElementById(
        "title"
    ).value;

    const description =
    document.getElementById(
        "description"
    ).value;

    const priority =
    document.getElementById(
        "priority"
    ).value;

    await fetch(
        "/api/tasks/",
        {
            method:"POST",

            headers:{
                "Content-Type":
                "application/json",

                Authorization:
                `Bearer ${token}`
            },

            body:JSON.stringify({

                title,
                description,
                priority

            })

        }
    );

    location.reload();
}


// Logout

function logout(){

    localStorage.removeItem(
        "access"
    );

    window.location.href="/";
}


loadDashboard();
loadTasks();