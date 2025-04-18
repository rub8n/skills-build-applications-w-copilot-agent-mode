import React, { useEffect, useState } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch('https://potential-fortnight-r444jqx5gr53vj5-8000.app.github.dev/workouts/')
      .then(response => response.json())
      .then(data => setWorkouts(data.data || data))
      .catch(error => console.error('Error fetching workouts:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Workouts</h1>
      <table className="table table-striped table-bordered">
        <thead className="table-dark">
          <tr>
            <th scope="col">#</th>
            <th scope="col">Workout Name</th>
            <th scope="col">Description</th>
          </tr>
        </thead>
        <tbody>
          {workouts.map((workout, index) => (
            <tr key={workout.id}>
              <th scope="row">{index + 1}</th>
              <td>{workout.name}</td>
              <td>{workout.description || 'No description available'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Workouts;