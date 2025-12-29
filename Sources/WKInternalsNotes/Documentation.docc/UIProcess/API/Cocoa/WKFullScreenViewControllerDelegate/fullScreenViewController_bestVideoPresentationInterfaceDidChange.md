# ``WKInternalsNotes/WKFullScreenViewControllerDelegate/fullScreenViewController(_:bestVideoPresentationInterfaceDidChange:)``

最適な動画プレゼンテーションインターフェースの変更を通知する。

## Objective-C Declaration
```objective-c
- (void)fullScreenViewController:(WKFullScreenViewController *)fullScreenViewController bestVideoPresentationInterfaceDidChange:(nullable WebCore::PlatformVideoPresentationInterface*)bestVideoPresentationInterface;
```

## Discussion
`WKFullScreenWindowControllerIOS` の実装では、visionOS で `_bestVideoPresentationModelClient` に新しいインターフェースをセットする。

## References
- [`WKFullScreenViewController.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L42)
- [`WKFullScreenWindowControllerIOS.mm#L2255`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L2255)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
