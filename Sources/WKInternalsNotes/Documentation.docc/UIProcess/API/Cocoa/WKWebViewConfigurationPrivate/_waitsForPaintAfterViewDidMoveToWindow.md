# ``WKInternalsNotes/WKWebViewConfiguration/_waitsForPaintAfterViewDidMoveToWindow``

view が window に入った後の paint を待つ

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setWaitsForPaintAfterViewDidMoveToWindow:) BOOL _waitsForPaintAfterViewDidMoveToWindow WK_API_AVAILABLE(macos(10.12.4), ios(10.3));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_waitsForPaintAfterViewDidMoveToWindow = YES`: view が window に入った後の paint を待つ。
- `_waitsForPaintAfterViewDidMoveToWindow = NO`: view が window に入った後の paint を待つ（無効）。

## References
- [`WKWebViewConfigurationPrivate.h#L91`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L91)
- [`WKWebViewConfiguration.mm#L1219`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1219)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
