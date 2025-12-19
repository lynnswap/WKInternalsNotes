# ``WKInternalsNotes/WKWebsiteDataRecord/_dataSize``

記録されているデータサイズを返す。

## Objective-C Declaration
```objective-c
@property (nullable, nonatomic, readonly) _WKWebsiteDataSize *_dataSize;
```

## Default Value
`websiteDataRecord().size` が未設定の場合は `nil`。

## Discussion
内部 `websiteDataRecord().size` を参照し、値があれば `_WKWebsiteDataSize` を生成して返す。

## References
- [`WKWebsiteDataRecordPrivate.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataRecordPrivate.h#L45)
- [`WKWebsiteDataRecord.mm#L155`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataRecord.mm#L155)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
