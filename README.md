# E-Learning Platform

This is a simple, frontend-only learning platform built with HTML, JavaScript, and Tailwind CSS. It provides an interactive interface for users to browse courses and watch video lessons with progress tracking.

## Features

- **Course Catalog**: Display course cards with descriptions, instructor info, and progress indicators
- **Video Player**: Watch lessons in a modal overlay with progress tracking
- **Progress Tracking**: 
  - Automatically saves your progress as you watch videos
  - Displays progress bars for each course
  - Marks lessons as completed
- **Responsive Design**: Works well on both desktop and mobile devices
- **Local Storage**: Remembers your progress between visits

## Technologies Used

- HTML5
- JavaScript (Vanilla)
- Tailwind CSS
- Font Awesome icons
- Local Storage API

## Usage

1. Open `index.html` in any modern web browser
2. Browse the available courses
3. Click on a lesson to start watching
4. Progress is automatically saved as you watch
5. Mark lessons as completed when you're done

## Customization

The platform can be easily customized by modifying the `platformConfig` object in the JavaScript section:

- Change platform title
- Add or modify courses
- Update course details (instructor, duration, images)
- Add new lessons with video URLs

## Future Improvements

- User authentication
- Course search functionality
- Quiz/assessment features
- Backend integration
- Course completion certificates