import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('https://potential-fortnight-r444jqx5gr53vj5-8000.app.github.dev/teams/')
      .then(response => response.json())
      .then(data => setTeams(data.data))
      .catch(error => console.error('Error fetching teams:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Teams</h1>
      <table className="table table-striped table-bordered">
        <thead className="table-dark">
          <tr>
            <th scope="col">#</th>
            <th scope="col">Team Name</th>
            <th scope="col">Members</th>
          </tr>
        </thead>
        <tbody>
          {teams.map((team, index) => (
            <tr key={team.id}>
              <th scope="row">{index + 1}</th>
              <td>{team.name}</td>
              <td>{JSON.parse(team.members).join(', ') || 'No members'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Teams;