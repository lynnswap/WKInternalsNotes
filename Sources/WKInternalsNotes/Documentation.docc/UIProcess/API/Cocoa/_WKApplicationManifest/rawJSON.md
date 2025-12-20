# ``WKInternalsNotes/_WKApplicationManifest/rawJSON``

マニフェストの生 JSON 文字列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable, copy) NSString *rawJSON;
```

## Discussion
`ApplicationManifest` の `rawJSON` を `NSString` に変換して返す（`null` の場合は `nil`）。

## References
- [`_WKApplicationManifest.h#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L75)
- [`_WKApplicationManifest.mm#L367`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L367)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
