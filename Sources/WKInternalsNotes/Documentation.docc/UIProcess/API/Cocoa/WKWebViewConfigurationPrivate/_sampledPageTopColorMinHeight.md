# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_sampledPageTopColorMinHeight``

page top color sampling の最小高さ

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setSampledPageTopColorMinHeight:) double _sampledPageTopColorMinHeight WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Default Value
iOS: `0` / macOS: `0`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- 値を変更すると: page top color sampling の最小高さの設定値として、その値が使われる。

## Details
- `0` は制約なし

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L165`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L165)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1527`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1527)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
