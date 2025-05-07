import React, { useEffect, useState } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch('https://psychic-barnacle-5g56q7jj496qc7qwx-8000.app.github.dev/api/leaderboard/')
      .then(res => res.json())
      .then(data => setLeaderboard(data));
  }, []);

  return (
    <div>
      <h2>Leaderboard</h2>
      <ul className="list-group">
        {leaderboard.map(entry => (
          <li key={entry._id} className="list-group-item">
            <strong>User:</strong> {entry.user} | <strong>Score:</strong> {entry.score}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Leaderboard;
