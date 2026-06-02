import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { VideoUpload } from "./components/video-upload/video-upload";

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, VideoUpload],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('video_transcode_ui');
}
