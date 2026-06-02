// src/app/services/video-upload.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class VideoUploadService {
  private apiUrl = 'http://localhost:8000/upload-url/'; // Your Django URL

  constructor(private http: HttpClient) { }

  // Get the Pre-signed URL
  getPresignedUrl(email: string, dimension: string): Observable<any> {
    return this.http.post(this.apiUrl, { email, dimension });
  }

  // Upload the file to S3 using the received URL
  uploadToS3(url: string, file: File): Observable<any> {
    return this.http.put(url, file, {
      headers: { 'Content-Type': 'video/mp4' }
    });
  }
}