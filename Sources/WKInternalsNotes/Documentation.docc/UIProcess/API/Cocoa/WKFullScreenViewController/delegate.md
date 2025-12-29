# ``WKInternalsNotes/WKFullScreenViewController/delegate``

フルスクリーン UI の通知先を設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id <WKFullScreenViewControllerDelegate> delegate;
```

## Default Value
初期値は `nil`。

## Discussion
getter/setter は弱参照を保持するだけ。`showUI`/`hideUI`/`invalidate` などで delegate メソッドが呼ばれる。

## References
- [`WKFullScreenViewController.mm#L264`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L264)
- [`WKFullScreenViewController.mm#L293`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L293)
- [`WKFullScreenViewController.mm#L319`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L319)
- [`WKFullScreenViewController.mm#L235`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L235)
- [`WKFullScreenViewController.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L47)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
