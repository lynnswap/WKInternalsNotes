# ``WKInternalsNotes/WKFullScreenViewController/hideBanner()``

フルスクリーン解除の警告バナーを非表示にする。

## Objective-C Declaration
```objective-c
- (void)hideBanner;
```

## Discussion
`ENABLE(FULLSCREEN_DISMISSAL_GESTURES)` のときのみ動作し、フェードアウト後にバナーを隠す。

## References
- [`WKFullScreenViewController.mm#L372`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L372)
- [`WKFullScreenViewController.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L61)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
