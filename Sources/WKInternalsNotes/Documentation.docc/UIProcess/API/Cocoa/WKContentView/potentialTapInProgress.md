# ``WKInternalsNotes/WKContentView/potentialTapInProgress``

潜在的なタップ処理中かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isPotentialTapInProgress) BOOL potentialTapInProgress;
```

## Default Value
`_potentialTapInProgress` を返す。

## Discussion
`_potentialTapInProgress` の値をそのまま返す。

## References
- [`WKContentViewInteraction.h#L547`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L547)
- [`WKContentViewInteraction.mm#L3871`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L3871)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
