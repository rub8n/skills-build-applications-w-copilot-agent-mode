import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://potential-fortnight-r444jqx5gr53vj5-8000.app.github.dev/activities/')
      .then(response => response.json())
      .then(data => setActivities(data.data || data))
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Activities</h1>
      <table className="table table-striped table-bordered">
        <thead className="table-dark">
          <tr>
            <th scope="col">#</th>
            <th scope="col">Activity Name</th>
            <th scope="col">Duration (minutes)</th>
            <th scope="col">Date</th>
            <th scope="col">User</th>
          </tr>
        </thead>
        <tbody>
          {activities && activities.map((activity, index) => (
            <tr key={activity.id}>
              <th scope="row">{index + 1}</th>
              <td>{activity.type}</td>
              <td>{activity.duration}</td>
              <td>{activity.date}</td>
              <td>{activity.user}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Activities;