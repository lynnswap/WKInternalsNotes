# ``WKInternalsNotes/_WKContextMenuElementInfo/hitTestResult``

コンテキストメニュー対象のヒットテスト結果を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) _WKHitTestResult *hitTestResult WK_API_AVAILABLE(macos(13.3));
```

## Default Value
`ContextMenuContextData` の `WebHitTestResultData` から都度生成される。

## Discussion
`_contextMenuElementInfoMac->hitTestResultData()` と `page()` を使って `API::HitTestResult::create` で生成し、`_WKHitTestResult` として返す。

## References
- [`_WKContextMenuElementInfo.mm#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContextMenuElementInfo.mm#L53)
- [`APIContextMenuElementInfoMac.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIContextMenuElementInfoMac.h#L48)
- [`_WKContextMenuElementInfo.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContextMenuElementInfo.h#L37)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
