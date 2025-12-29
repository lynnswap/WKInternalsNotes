# ``WKInternalsNotes/_WKResourceLoadStatisticsFirstParty/timeLastUpdated``

内部の統計データが保持する最終更新時刻を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSTimeInterval timeLastUpdated;
```

## Default Value
`API::ResourceLoadStatisticsFirstParty::timeLastUpdated()` の値。

## Discussion
内部の `_firstParty` から `timeLastUpdated()` を取得して返す。

## References
- [`_WKResourceLoadStatisticsFirstParty.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadStatisticsFirstParty.h#L38)
- [`_WKResourceLoadStatisticsFirstParty.mm#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadStatisticsFirstParty.mm#L51)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
