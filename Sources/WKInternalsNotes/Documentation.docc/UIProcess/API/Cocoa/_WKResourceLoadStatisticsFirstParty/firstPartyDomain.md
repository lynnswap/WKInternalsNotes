# ``WKInternalsNotes/_WKResourceLoadStatisticsFirstParty/firstPartyDomain``

ファーストパーティのドメイン文字列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *firstPartyDomain;
```

## Default Value
`API::ResourceLoadStatisticsFirstParty::firstPartyDomain()` の値。

## Discussion
内部の `_firstParty` から `firstPartyDomain()` を取得し、`NSString` に変換して返す。

## References
- [`_WKResourceLoadStatisticsFirstParty.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadStatisticsFirstParty.h#L36)
- [`_WKResourceLoadStatisticsFirstParty.mm#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadStatisticsFirstParty.mm#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
