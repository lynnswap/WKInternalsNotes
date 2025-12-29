# ``WKInternalsNotes/_WKContextMenuElementInfo/qrCodePayloadString``

QRコードのペイロード文字列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy, nullable) NSString *qrCodePayloadString WK_API_AVAILABLE(macos(14.0));
```

## Default Value
空文字列の場合は `nil`。

## Discussion
`ContextMenuContextData` 由来の `qrCodePayloadString` を取得し、空文字列の場合は `nil` を返す。

## References
- [`_WKContextMenuElementInfo.mm#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContextMenuElementInfo.mm#L60)
- [`APIContextMenuElementInfoMac.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIContextMenuElementInfoMac.h#L50)
- [`_WKContextMenuElementInfo.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContextMenuElementInfo.h#L38)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
