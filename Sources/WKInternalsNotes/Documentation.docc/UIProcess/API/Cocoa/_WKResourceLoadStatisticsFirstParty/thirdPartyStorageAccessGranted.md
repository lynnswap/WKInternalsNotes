# ``WKInternalsNotes/_WKResourceLoadStatisticsFirstParty/thirdPartyStorageAccessGranted``

サードパーティのストレージアクセス許可状態を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL thirdPartyStorageAccessGranted;
```

## Default Value
`API::ResourceLoadStatisticsFirstParty::storageAccess()` の値。

## Discussion
実装では `-storageAccess` が定義されており、内部の `storageAccess()` を返す。

## References
- [`_WKResourceLoadStatisticsFirstParty.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadStatisticsFirstParty.h#L37)
- [`_WKResourceLoadStatisticsFirstParty.mm#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadStatisticsFirstParty.mm#L46)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
