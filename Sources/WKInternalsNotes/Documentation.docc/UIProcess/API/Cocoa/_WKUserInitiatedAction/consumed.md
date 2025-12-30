# ``WKInternalsNotes/_WKUserInitiatedAction/consumed``

消費済みかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isConsumed) BOOL consumed;
```

## Default Value
`NO`（`m_consumed` の初期値は `false`）。

## Discussion
内部の `API::UserInitiatedAction` が保持する `m_consumed` を `consumed()` 経由で返す。

## References
- [`_WKUserInitiatedAction.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserInitiatedAction.h#L36)
- [`_WKUserInitiatedAction.mm#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserInitiatedAction.mm#L61)
- [`APIUserInitiatedAction.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIUserInitiatedAction.h#L50)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
