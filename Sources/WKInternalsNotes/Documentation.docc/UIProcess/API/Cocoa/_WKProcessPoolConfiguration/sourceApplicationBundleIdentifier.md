# ``WKInternalsNotes/_WKProcessPoolConfiguration/sourceApplicationBundleIdentifier``

呼び出し元アプリの bundle identifier を表すが、現在は getter が常に `nil` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSString *sourceApplicationBundleIdentifier WK_API_DEPRECATED_WITH_REPLACEMENT("_WKWebsiteDataStoreConfiguration.sourceApplicationBundleIdentifier", macos(10.12.3, 10.14.4), ios(10.3, 12.2));
```

## Default Value
初期値は `nil`（getter は常に `nil` を返す）。

## Discussion
`_WKProcessPoolConfiguration.mm` の getter は `nil` を返し、setter は空実装のため値は保存されない。

## References
- [`_WKProcessPoolConfiguration.mm#L196`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L196)
- [`_WKProcessPoolConfiguration.mm#L201`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L201)
- [`_WKProcessPoolConfiguration.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.h#L60)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
