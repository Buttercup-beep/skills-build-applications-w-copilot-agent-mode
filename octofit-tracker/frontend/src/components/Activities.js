
import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://psychic-barnacle-5g56q7jj496qc7qwx-8000.app.github.dev/api/activities/')
      .then(res => res.json())
      .then(data => setActivities(data));
  }, []);

  return (
    <div className="container mt-4">
      <div className="card shadow">
        <div className="card-body">
          <h1 className="card-title display-5 mb-4 text-primary">Activities</h1>
          <div className="table-responsive">
            <table className="table table-striped table-hover">
              <thead className="table-dark">
                <tr>
                  <th>Type</th>
                  <th>User</th>
                  <th>Duration (min)</th>
                </tr>
              </thead>
              <tbody>
                {activities.map(activity => (
                  <tr key={activity._id}>
                    <td>{activity.activity_type}</td>
                    <td>{activity.user}</td>
                    <td>{activity.duration}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Activities;
