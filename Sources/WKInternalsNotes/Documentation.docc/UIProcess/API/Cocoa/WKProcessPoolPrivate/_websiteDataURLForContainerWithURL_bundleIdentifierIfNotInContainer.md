# ``WKInternalsNotes/WKProcessPool/_websiteDataURLForContainerWithURL(_:bundleIdentifierIfNotInContainer:)``

コンテナ URL と bundle ID から WebsiteData の URL を生成する。

## Objective-C Declaration
```objective-c
+ (NSURL *)_websiteDataURLForContainerWithURL:(NSURL *)containerURL bundleIdentifierIfNotInContainer:(NSString *)bundleIdentifier;
```

## Discussion
`containerURL/Library/WebKit` に `WebsiteData` を付加し、コンテナが無い場合は bundleIdentifier を挟む。

## References
- [`WKProcessPoolPrivate.h#L106`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L106)
- [`WKProcessPool.mm#L213`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L213)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
