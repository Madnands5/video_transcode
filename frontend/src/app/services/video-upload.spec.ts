import { TestBed } from '@angular/core/testing';

import { VideoUpload } from './video-upload';

describe('VideoUpload', () => {
  let service: VideoUpload;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(VideoUpload);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
