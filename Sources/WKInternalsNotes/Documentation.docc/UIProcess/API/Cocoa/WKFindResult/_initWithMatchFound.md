# ``WKInternalsNotes/WKFindResult/_initWithMatchFound(_:)``

検索結果の一致有無を設定する内部初期化子。

## Objective-C Declaration
```objective-c
- (instancetype)_initWithMatchFound:(BOOL)matchFound;
```

## Discussion
`_matchFound` に `matchFound` を設定して返す。

## References
- [`WKFindResultInternal.h#L30`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFindResultInternal.h#L30)
- [`WKFindResult.mm#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFindResult.mm#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
