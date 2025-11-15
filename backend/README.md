# ṚtaFlow

> *"Order, rhythm, and focus — aligned with Ṛta."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg)](https://fastapi.tiangolo.com/)

ṚtaFlow is an open-source, privacy-first journaling and task management application designed to run locally with optional cloud sync. Built with a focus on minimalism, performance, and user privacy, ṚtaFlow provides a seamless experience for organizing your thoughts and tasks.

---

## 🌟 Features

- **📝 Journaling**: Daily entries with markdown support
- **✅ Task Management**: Create, organize, and track tasks efficiently
- **🔒 Privacy-First**: All data stored locally by default
- **⚡ Lightweight**: Minimal resource footprint (target: under 150 MB)
- **🌐 Offline-Capable**: Full functionality without internet connection
- **🔄 Optional Sync**: Cloud sync capabilities when needed
- **🎨 Clean UI**: Intuitive, distraction-free interface

---

## 🏗️ Architecture

ṚtaFlow is built using a modern, modular tech stack:

### Backend
- **FastAPI**: High-performance Python web framework
- **SQLite**: Lightweight, serverless database
- **Python 3.11+**: Modern Python features and performance

### Frontend *(Planned)*
- **React**: Component-based UI library
- **Zustand**: Lightweight state management
- **Vite**: Next-generation frontend tooling

### Desktop Wrapper *(Planned)*
- **Tauri**: Rust-based desktop application framework
- Provides native performance with web technologies

---

## 📂 Project Structure

```
RtaFlow/
├── backend/              # FastAPI backend server
│   ├── app/             # Application code
│   ├── tests/           # Backend tests
│   └── requirements.txt # Python dependencies
├── scripts/             # Development and deployment scripts
├── pytest.ini          # Pytest configuration
├── test_db.sqlite      # Test database
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/akshat1903kk/RtaFlow.git
   cd RtaFlow
   ```

2. **Set up the backend**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Run the development server**
   ```bash
   cd backend
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://localhost:8000`

4. **Access API documentation**
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

### Quick Start Script *(Coming Soon)*
```bash
./scripts/run_dev.sh
```

---

## 🧪 Testing

Run the test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=backend/app
```

---

## 🗺️ Roadmap

### Phase 1: Core Backend (Current)
- [x] FastAPI server setup
- [x] SQLite database integration
- [x] Basic project structure
- [ ] User authentication
- [ ] Journal entry CRUD operations
- [ ] Task management endpoints
- [ ] API documentation

### Phase 2: Frontend Development
- [ ] React application setup
- [ ] Zustand state management
- [ ] Journal entry interface
- [ ] Task management UI
- [ ] Responsive design
- [ ] Dark mode support

### Phase 3: Desktop Application
- [ ] Tauri integration
- [ ] Native desktop features
- [ ] System tray integration
- [ ] Local file system access
- [ ] Cross-platform build system

### Phase 4: Advanced Features
- [ ] Data encryption
- [ ] Cloud sync (optional)
- [ ] Export/import functionality
- [ ] Tags and categories
- [ ] Search functionality
- [ ] Custom themes
- [ ] Plugin system

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code
- Write tests for new features
- Update documentation as needed
- Keep commits atomic and descriptive

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Inspired by the concept of **Ṛta** (ऋत) - the Vedic principle of natural order and rhythm
- Built with modern open-source technologies
- Community-driven development

---

## 📬 Contact

**Akshat** - [@akshat1903kk](https://github.com/akshat1903kk)

Project Link: [https://github.com/akshat1903kk/RtaFlow](https://github.com/akshat1903kk/RtaFlow)

---

## ⭐ Star History

If you find ṚtaFlow useful, please consider giving it a star! It helps the project grow and motivates continued development.

---

<div align="center">
  <sub>Built with ❤️ for productivity and mindfulness</sub>
</div>
