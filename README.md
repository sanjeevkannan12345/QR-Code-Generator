# QR Code Generator

A simple Python script that generates a QR code from any website URL or text input, and saves it as a PNG image.

## Features

- Takes any website link or plain text as input
- Generates a scannable QR code image
- Saves the output as `my_qrcode.png`
- Lightweight — built with the `qrcode` Python library

## Tech Stack

- **Language:** Python 3
- **Library:** [qrcode](https://pypi.org/project/qrcode/)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/QR-Code-Generator.git
   cd QR-Code-Generator
   ```

2. Install the required dependency:
   ```bash
   pip install qrcode[pil]
   ```

## Usage

Run the script:
```bash
python QR-Code-Generator.py
```

You'll be prompted to enter a website URL or any text:
```
Enter website or text: https://web.whatsapp.com/
QR Code generated successfully!
```

The QR code image will be saved as `my_qrcode.png` in the same directory.

## Example

| Input | Output |
|-------|--------|
| `https://web.whatsapp.com/` | A scannable QR code linking to WhatsApp Web |

## Future Improvements

- Add custom output filename support
- Add color/logo customization for the QR code
- Build a simple GUI using Tkinter
- Add error handling for empty input

## Author

**Sanjeev**
B.Sc. Digital and Cyber Forensic Science, Rathinam Global University

## License

This project is open source and available under the [MIT License](LICENSE).
