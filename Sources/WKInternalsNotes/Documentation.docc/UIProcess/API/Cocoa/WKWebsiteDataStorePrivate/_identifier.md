# ``WKInternalsNotes/WKWebsiteDataStore/_identifier``

データストアの識別子を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSUUID *_identifier;
```

## Default Value
configuration に identifier がない場合は `nil`。

## Discussion
`configuration().identifier()` を取得し、存在すれば `NSUUID` として返す。

## References
- [`WKWebsiteDataStorePrivate.h#L151`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L151)
- [`WKWebsiteDataStore.mm#L1473`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1473)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
