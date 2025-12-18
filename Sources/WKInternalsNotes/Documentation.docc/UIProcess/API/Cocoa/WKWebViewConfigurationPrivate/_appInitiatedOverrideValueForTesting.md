# ``WKInternalsNotes/WKWebViewConfiguration/_appInitiatedOverrideValueForTesting``

attribution override（テスト用）

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAppInitiatedOverrideValueForTesting:) _WKAttributionOverrideTesting _appInitiatedOverrideValueForTesting WK_API_AVAILABLE(ios(15.0));
```

## Default Value
iOS: `_WKAttributionOverrideTestingNoOverride`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- 値を変更すると: attribution override（テスト用）のモード/値として、その enum 値が使われる。

## Details
- テスト用

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L124`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L124)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L974`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L974)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
