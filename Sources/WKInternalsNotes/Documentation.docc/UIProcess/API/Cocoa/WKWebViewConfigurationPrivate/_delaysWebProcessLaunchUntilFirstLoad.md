# ``WKInternalsNotes/WKWebViewConfiguration/_delaysWebProcessLaunchUntilFirstLoad``

初回ロードまで WebProcess 起動を遅延

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setDelaysWebProcessLaunchUntilFirstLoad:) BOOL _delaysWebProcessLaunchUntilFirstLoad WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Default Value
iOS: `NO` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_delaysWebProcessLaunchUntilFirstLoad = YES`: 初回ロードまで WebProcess 起動を遅延。
- `_delaysWebProcessLaunchUntilFirstLoad = NO`: 初回ロードまで WebProcess 起動を遅延（無効）。

## Details
- `WebProcessPool::globalDelaysWebProcessLaunchDefaultValue()`

## References
- [`WKWebViewConfigurationPrivate.h#L157`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L157)
- [`WKWebViewConfiguration.mm#L1469`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1469)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
