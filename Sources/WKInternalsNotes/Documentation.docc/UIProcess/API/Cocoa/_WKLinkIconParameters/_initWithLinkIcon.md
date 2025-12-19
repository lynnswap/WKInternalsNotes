# ``WKInternalsNotes/_WKLinkIconParameters/_initWithLinkIcon(_:)``

`WebCore::LinkIcon` からリンクアイコン情報を構築する。

## Objective-C Declaration
```objective-c
- (instancetype)_initWithLinkIcon:(const WebCore::LinkIcon&)linkIcon;
```

## Discussion
`linkIcon` の URL / MIME type / size / type / attributes を読み取り、`_WKLinkIconParameters` の各プロパティに変換して保持する。

## References
- [`_WKLinkIconParametersInternal.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKLinkIconParametersInternal.h#L34)
- [`_WKLinkIconParameters.mm#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKLinkIconParameters.mm#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
