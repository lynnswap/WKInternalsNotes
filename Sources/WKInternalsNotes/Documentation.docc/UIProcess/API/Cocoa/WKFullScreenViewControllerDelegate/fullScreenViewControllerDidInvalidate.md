# ``WKInternalsNotes/WKFullScreenViewControllerDelegate/fullScreenViewControllerDidInvalidate(_:)``

フルスクリーンビューの無効化を通知する。

## Objective-C Declaration
```objective-c
- (void)fullScreenViewControllerDidInvalidate:(WKFullScreenViewController *)fullScreenViewController;
```

## Discussion
`WKFullScreenWindowControllerIOS` の実装では、visionOS かつ「ベスト動画フルスクリーン」ではない場合に、`_bestVideoPresentationModelClient` をリセットする。

## References
- [`WKFullScreenViewController.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L40)
- [`WKFullScreenWindowControllerIOS.mm#L2246`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L2246)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
