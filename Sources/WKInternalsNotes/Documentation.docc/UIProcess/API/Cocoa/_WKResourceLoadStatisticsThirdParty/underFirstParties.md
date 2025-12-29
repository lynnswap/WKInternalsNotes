# ``WKInternalsNotes/_WKResourceLoadStatisticsThirdParty/underFirstParties``

関連する First Party の一覧を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSArray<_WKResourceLoadStatisticsFirstParty *> *underFirstParties;
```

## Default Value
`API::ResourceLoadStatisticsThirdParty::underFirstParties()` の値。

## Discussion
`_thirdParty->underFirstParties()` を `_WKResourceLoadStatisticsFirstParty` に変換して配列で返す。

## References
- [`_WKResourceLoadStatisticsThirdParty.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadStatisticsThirdParty.h#L39)
- [`_WKResourceLoadStatisticsThirdParty.mm#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadStatisticsThirdParty.mm#L48)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
