# ``WKInternalsNotes/WKScrollView/_contentInsetWasExternallyOverridden``

外部から `contentInset` が設定されたかを示す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _contentInsetWasExternallyOverridden;
```

## Default Value
初期は `NO`。`setContentInset:` が呼ばれると `YES` になる。

## Discussion
外部指定の有無を保持するフラグで、内部の inset 更新の可否判断に使われる。

## References
- [`WKScrollView.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L48)
- [`WKScrollView.mm#L328`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L328)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
