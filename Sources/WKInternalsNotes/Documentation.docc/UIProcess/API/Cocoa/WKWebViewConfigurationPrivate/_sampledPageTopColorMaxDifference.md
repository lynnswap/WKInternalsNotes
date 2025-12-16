# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_sampledPageTopColorMaxDifference``

page top color sampling の許容差分

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setSampledPageTopColorMaxDifference:) double _sampledPageTopColorMaxDifference WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Default Value
iOS: `0` / macOS: `0`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- 値を変更すると: page top color sampling の許容差分の設定値として、その値が使われる。

## Details
- `0` は sampling 無効

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L161`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L161)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1517`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1517)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
