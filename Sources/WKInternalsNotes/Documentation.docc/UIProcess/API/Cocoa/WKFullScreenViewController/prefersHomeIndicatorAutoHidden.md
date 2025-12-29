# ``WKInternalsNotes/WKFullScreenViewController/prefersHomeIndicatorAutoHidden``

ホームインジケータの自動非表示を希望するかを設定/取得する。

## Objective-C Declaration
```objective-c
@property (assign, nonatomic) BOOL prefersHomeIndicatorAutoHidden;
```

## Default Value
初期値は `NO`。

## Discussion
setter は `_prefersHomeIndicatorAutoHidden` を更新し、Apple TV 以外では `setNeedsUpdateOfHomeIndicatorAutoHidden` を呼ぶ。

## References
- [`WKFullScreenViewController.mm#L666`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L666)
- [`WKFullScreenViewController.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L50)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
