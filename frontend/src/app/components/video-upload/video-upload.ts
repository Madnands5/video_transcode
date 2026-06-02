import { Component } from '@angular/core';
import { VideoUploadService } from '../../services/video-upload';
import { FormsModule } from '@angular/forms';
@Component({
  selector: 'app-video-upload',
  imports: [FormsModule],
  templateUrl: './video-upload.html',
  styleUrl: './video-upload.css',
})
export class VideoUpload {
  selectedFile: File | null = null;
  email: string = '';
  dimension: string = '1080p';

  constructor(private uploadService: VideoUploadService) { }

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  onSubmit() {
    if (!this.selectedFile) return;

    // Step 1: Get URL from Django
    this.uploadService.getPresignedUrl(this.email, this.dimension).subscribe(res => {
      const { url } = res;

      // Step 2: Upload directly to S3/LocalStack
      this.uploadService.uploadToS3(url, this.selectedFile!).subscribe({
        next: () => alert('Upload Successful!'),
        error: (err: Error) => console.error('Upload failed', err)
      });
    });
  }
}
