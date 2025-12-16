# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_alternateWebViewForNavigationGestures``

ナビゲーションジェスチャの代替 `WKWebView`

## Objective-C Declaration
```objective-c
@property (nonatomic, weak, setter=_setAlternateWebViewForNavigationGestures:) WKWebView *_alternateWebViewForNavigationGestures;
```

## Default Value
iOS: `nil` / macOS: `nil`

## Discussion
- この API を使わない場合: back/forward ナビゲーションジェスチャは、この `WKWebView` 自身の back-forward list を使う。
- `_alternateWebViewForNavigationGestures` を設定すると: iOS の swipe ジェスチャが参照する back-forward list の “source page” を差し替えられる。
- `nil` に戻すと: 差し替えを解除する。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L72)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L700`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L700)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
