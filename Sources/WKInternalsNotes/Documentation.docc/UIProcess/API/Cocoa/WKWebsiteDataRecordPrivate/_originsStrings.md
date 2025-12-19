# ``WKInternalsNotes/WKWebsiteDataRecord/_originsStrings()``

記録されている origin を文字列配列で返す。

## Objective-C Declaration
```objective-c
- (NSArray<NSString *> *)_originsStrings WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
`websiteDataRecord().origins` を `origin.toString()` で `NSString` に変換して配列化する。

## References
- [`WKWebsiteDataRecordPrivate.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataRecordPrivate.h#L47)
- [`WKWebsiteDataRecord.mm#L165`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataRecord.mm#L165)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
