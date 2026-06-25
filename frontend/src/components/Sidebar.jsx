import {
  FaPlus,
  FaCog,
  FaRobot,
} from "react-icons/fa";

function Sidebar({
  chats,
  onNewChat,
}) {
  return (
    <div className="sidebar">
      <div>
        <h2>
          <FaRobot /> Jarvis
        </h2>

        <button
          className="new-chat"
          onClick={onNewChat}
        >
          <FaPlus />
          New Chat
        </button>

        <div className="history">
          {chats.map((chat, i) => (
            <div
              key={i}
              className="history-item"
            >
              💬 {chat}
            </div>
          ))}
        </div>
      </div>

      <div className="settings">
        <FaCog /> Prince Giri
      </div>
    </div>
  );
}

export default Sidebar;