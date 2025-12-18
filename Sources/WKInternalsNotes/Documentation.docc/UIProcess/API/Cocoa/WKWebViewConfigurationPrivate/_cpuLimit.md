# ``WKInternalsNotes/WKWebViewConfiguration/_cpuLimit``

CPU リミット（macOS のみ）

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite, setter=_setCPULimit:) double _cpuLimit WK_API_AVAILABLE(macos(10.13.4));
```

## Default Value
iOS: `N/A` / macOS: `0`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- 値を変更すると: CPU リミット（macOS のみ）の設定値として、その値が使われる。

## Details
- `0` は未設定相当

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L131`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L131)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1314`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1314)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
