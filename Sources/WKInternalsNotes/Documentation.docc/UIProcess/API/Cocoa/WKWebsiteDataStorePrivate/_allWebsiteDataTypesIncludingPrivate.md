# ``WKInternalsNotes/WKWebsiteDataStore/_allWebsiteDataTypesIncludingPrivate()``

公開 + private の Website Data Type をまとめたセットを返す。

## Objective-C Declaration
```objective-c
+ (NSSet<NSString *> *)_allWebsiteDataTypesIncludingPrivate;
```

## Discussion
`allWebsiteDataTypes` に private type（HSTS/ResourceLoadStatistics/Credentials/AdClickAttributions/PrivateClickMeasurements/AlternativeServices）を追加したセットを `dispatch_once` で構築して返す。

## References
- [`WKWebsiteDataStorePrivate.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L52)
- [`WKWebsiteDataStore.mm#L734`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L734)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
