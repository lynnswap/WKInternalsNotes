# ``WKInternalsNotes/WKProcessPool/_websiteDataURLForContainerWithURL(_:)``

コンテナ URL から WebsiteData の URL を生成する。

## Objective-C Declaration
```objective-c
+ (NSURL *)_websiteDataURLForContainerWithURL:(NSURL *)containerURL;
```

## Discussion
`bundleIdentifierIfNotInContainer:nil` で `_websiteDataURLForContainerWithURL:bundleIdentifierIfNotInContainer:` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L105`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L105)
- [`WKProcessPool.mm#L213`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L213)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
