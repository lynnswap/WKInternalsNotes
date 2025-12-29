# ``WKInternalsNotes/WKFullScreenViewController/showBanner()``

フルスクリーン解除の警告バナーを表示する。

## Objective-C Declaration
```objective-c
- (void)showBanner;
```

## Discussion
`ENABLE(FULLSCREEN_DISMISSAL_GESTURES)` のときのみ動作し、バナーを表示して `autoHideDelay` 後に `hideBanner` を予約する。

## References
- [`WKFullScreenViewController.mm#L355`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L355)
- [`WKFullScreenViewController.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L60)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
