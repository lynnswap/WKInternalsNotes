# ``WKInternalsNotes/_WKApplicationManifest/applicationDescription``

アプリケーションの説明文を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable, copy) NSString *applicationDescription;
```

## Discussion
`ApplicationManifest` の `description` を `NSString` に変換して返す（`null` の場合は `nil`）。

## References
- [`_WKApplicationManifest.h#L79`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L79)
- [`_WKApplicationManifest.mm#L398`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L398)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
