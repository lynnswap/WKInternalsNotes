# ``WKInternalsNotes/WKWebViewConfiguration/_incrementalRenderingSuppressionTimeout``

incremental rendering 抑制のタイムアウト（秒）

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setIncrementalRenderingSuppressionTimeout:) NSTimeInterval _incrementalRenderingSuppressionTimeout WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `5` / macOS: `5`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- 値を変更すると: incremental rendering 抑制のタイムアウト（秒）の設定値として、その値が使われる。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L76)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L745`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L745)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
