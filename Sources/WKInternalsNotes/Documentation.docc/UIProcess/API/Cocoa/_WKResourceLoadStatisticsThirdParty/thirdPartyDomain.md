# ``WKInternalsNotes/_WKResourceLoadStatisticsThirdParty/thirdPartyDomain``

サードパーティドメインを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *thirdPartyDomain;
```

## Default Value
`API::ResourceLoadStatisticsThirdParty::thirdPartyDomain()` の値。

## Discussion
内部の `_thirdParty` から `thirdPartyDomain()` を取得して `NSString` 化して返す。

## References
- [`_WKResourceLoadStatisticsThirdParty.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadStatisticsThirdParty.h#L38)
- [`_WKResourceLoadStatisticsThirdParty.mm#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadStatisticsThirdParty.mm#L43)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
