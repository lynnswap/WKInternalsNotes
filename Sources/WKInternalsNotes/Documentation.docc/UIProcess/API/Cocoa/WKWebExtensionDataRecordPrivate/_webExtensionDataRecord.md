# ``WKInternalsNotes/WKWebExtensionDataRecord/_webExtensionDataRecord``

内部の `WebKit::WebExtensionDataRecord` 参照を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WebKit::WebExtensionDataRecord& _webExtensionDataRecord;
```

## Default Value
初期化後は内部 WebExtensionDataRecord への参照を保持するため `nil` にならない。

## Discussion
`_webExtensionDataRecord` を参照して返すだけで、`WKObject` 実装から内部 C++ オブジェクトへアクセスするために使われる。

## References
- [`WKWebExtensionDataRecordInternal.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionDataRecordInternal.h#L43)
- [`WKWebExtensionDataRecord.mm#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionDataRecord.mm#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
