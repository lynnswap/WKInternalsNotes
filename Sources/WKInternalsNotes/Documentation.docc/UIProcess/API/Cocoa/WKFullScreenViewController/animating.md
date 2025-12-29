# ``WKInternalsNotes/WKFullScreenViewController/animating``

フルスクリーン遷移のアニメーション中かを表す。

## Objective-C Declaration
```objective-c
@property (assign, nonatomic, getter=isAnimating) BOOL animating;
```

## Default Value
初期値は `NO`。

## Discussion
setter は `setNeedsStatusBarAppearanceUpdate` を呼び、アニメーション中は `hideUI`、終了時は `showUI` を呼ぶ。`prefersStatusBarHidden` の判定にも使われる。

## References
- [`WKFullScreenViewController.mm#L705`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L705)
- [`WKFullScreenViewController.mm#L975`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L975)
- [`WKFullScreenViewController.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L54)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
