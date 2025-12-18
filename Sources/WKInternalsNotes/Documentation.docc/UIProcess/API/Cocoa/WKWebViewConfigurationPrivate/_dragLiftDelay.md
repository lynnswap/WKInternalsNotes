# ``WKInternalsNotes/WKWebViewConfiguration/_dragLiftDelay``

ドラッグ開始（lift）までの遅延

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setDragLiftDelay:) _WKDragLiftDelay _dragLiftDelay WK_API_AVAILABLE(ios(11.0));
```

## Default Value
iOS: `_WKDragLiftDelayShort`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- 値を変更すると: ドラッグ開始（lift）までの遅延のモード/値として、その enum 値が使われる。

## Details
- `WebKitDebugDragLiftDelay` 未設定時

## References
- [`WKWebViewConfigurationPrivate.h#L118`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L118)
- [`WKWebViewConfiguration.mm#L254`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L254)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
